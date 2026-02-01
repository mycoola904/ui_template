from django.shortcuts import render


def dashboard(request):
    return render(request, "ui/pages/dashboard.html", {"active_nav": "dashboard"})

def tables(request):
    return render(request, "ui/pages/tables.html", {"active_nav": "tables"})

def forms(request):
    return render(request, "ui/pages/forms.html", {"active_nav": "forms"})



def table_demo(request):
    headers = [
        "Column 1",
        "Column 2",
        "Status",
        "Date",
    ]

    actions_html = (
        '<button class="btn btn-ghost btn-xs btn-square" type="button" aria-label="View">👁️</button>'
        '<button class="btn btn-ghost btn-xs btn-square" type="button" aria-label="Edit">✏️</button>'
        '<button class="btn btn-ghost btn-xs btn-square text-error" type="button" aria-label="Delete">🗑️</button>'
    )

    rows = [
        {
            "cells": [
                "Alpha",
                "Example Item",
                "Active",
                "01/12/2026",
            ],
            "href": "",  # placeholder for template demo
            "actions_html": actions_html,
        }
    ]

    return render(request, "ui/pages/table_demo.html", {
        "headers": headers,
        "rows": rows,
    })


