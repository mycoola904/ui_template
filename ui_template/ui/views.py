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

  

    rows = [
        {
            "cells": [
                "Alpha",
                "Example Item",
                "Active",
                "01/12/2026",
            ],
            "href": "",  # placeholder for template demo
            "actions_template": "ui/components/table_actions/default.html",
        }
    ]

    return render(request, "ui/pages/table_demo.html", {
        "headers": headers,
        "rows": rows,
    })


def panel_demo(request):
    context = {
        "panel_title": "Account Summary",
        "panel_subtitle": "Header panel that will sit above the transactions table",
        "panel_body_template": "ui/components/panel_bodies/account_header.html",
        "panel_footer_template": "ui/components/panel_footers/account_header_actions.html",

        "account_name": "Checking",
        "account_type": "Bank Account",
        "balance_display": "$2,481.19",
        "updated_display": "Jan 31, 2026",
    }
    return render(request, "ui/pages/panel_demo.html", context)

def account_detail_demo(request):
    # Panel config
    panel_context = {
        "panel_title": "Account Summary",
        "panel_subtitle": "Checking - Last updated Jan 31, 2026",
        "panel_body_template": "ui/components/panel_bodies/account_header.html",
        "panel_footer_template": "ui/components/panel_footers/account_header_actions.html",

        # Panel body vars
        "account_name": "Checking",
        "account_type": "Bank Account",
        "balance_display": "$2,481.19",
        "updated_display": "Jan 31, 2026",
    }

    # Table config
    headers = ["Date", "Description", "Category", "Amount", "Balance"]

    actions_template = "ui/components/table_actions/default.html"

    rows = [
        {
            "cells": ["01/31/2026", "Paycheck", "Income", "+$1,250.00", "$2,481.19"],
            "href": "",  # placeholder for demo
            "actions_template": actions_template,
        },
        {
            "cells": ["01/29/2026", "Grocery Store", "Groceries", "-$86.42", "$1,231.19"],
            "href": "",
            "actions_template": actions_template,
        },
        {
            "cells": ["01/28/2026", "Electric Bill", "Utilities", "-$142.10", "$1,317.61"],
            "href": "",
            "actions_template": actions_template,
        },
    ]

    context = {
        **panel_context,
        "headers": headers,
        "rows": rows,
        "actions": True,
        "empty_message": "No transactions",
    }

    return render(request, "ui/pages/account_detail_demo.html", context)





