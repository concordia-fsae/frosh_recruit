from django.db import models
from django.http import StreamingHttpResponse

import csv
from recruit_app.models import Team


def get_model_fields(model, ignore=None):
    '''
    ::param model, the Django model class to process
    ::ignore, an array of fields to ignore

    This function returns a list of field names from the given model
    '''

    model_fields = model._meta.get_fields()
    model_field_names = list(set([f.name for f in model_fields if \
                                (ignore is None) or \
                                (f.name not in ignore)]))

    return model_field_names


def qs_to_set(qs, fields=None, ignore=None):
    model_field_names = get_model_fields(qs.model, ignore)
    lookup_fields = None
    if fields is not None:
        for i in fields:
            if ("__" in i) or (i in model_field_names):
                lookup_fields.append(i)
    else:
        lookup_fields = model_field_names

    items = list(qs.values(*lookup_fields))
    items_merged = {}

    for item in items:
        if item["id"] not in items_merged:
            item_id = item.pop("id")
            items_merged[item_id] = item
            items_merged[item_id]["interests"] = [items_merged[item_id]["interests"]]
        else:
            items_merged[item["id"]]["interests"].append(item["interests"])

    for item in items_merged.values():
        teams = []
        for team in item["interests"]:
            if(not team is None):
                teams.append(Team.objects.filter(id=team)[0].team_name)
        teams.sort()
        teams = ", ".join(teams)
        item["interests"] = teams
    return list(items_merged.values())


class Echo:
    def write(self, value):
        return value


def export_csv(modeladmin, request, queryset):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = qs_to_set(queryset)
    rows = [{"first_name":"First Name", "last_name":"Last Name", "email":"Email Address", "interests":"Interested In", "program":"Program", "year":"Program Year"}] + rows
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow([row["first_name"], row["last_name"], row["email"], row["interests"], row["program"], row["year"]]) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response

export_csv.short_description = "Export the selected items to CSV"

