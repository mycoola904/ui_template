from django.shortcuts import render


def dashboard(request):
    due_accounts = [
        {
            "name": "Rent",
            "account": "Checking",
            "due": "Feb 04",
            "amount": "$1,420.00",
            "status": "High",
        },
        {
            "name": "Utilities",
            "account": "Checking",
            "due": "Feb 06",
            "amount": "$182.50",
            "status": "Medium",
        },
        {
            "name": "Car Insurance",
            "account": "Savings",
            "due": "Feb 07",
            "amount": "$96.00",
            "status": "Low",
        },
    ]

    budget_legend = [
        {"label": "Housing", "amount": "$1,420", "color": "#60a5fa"},
        {"label": "Food", "amount": "$520", "color": "#34d399"},
        {"label": "Utilities", "amount": "$210", "color": "#fbbf24"},
        {"label": "Other", "amount": "$180", "color": "#f87171"},
    ]
    budget_conic = (
        "conic-gradient("
        "#60a5fa 0 46%, "
        "#34d399 46% 73%, "
        "#fbbf24 73% 86%, "
        "#f87171 86% 100%"
        ")"
    )

    transactions = [
        {
            "date": "Feb 01",
            "account": "Checking",
            "description": "Coffee Shop",
            "amount": "-$6.40",
            "amount_class": "text-error",
        },
        {
            "date": "Jan 31",
            "account": "Checking",
            "description": "Payroll",
            "amount": "+$1,250.00",
            "amount_class": "text-success",
        },
        {
            "date": "Jan 30",
            "account": "Savings",
            "description": "Transfer In",
            "amount": "+$300.00",
            "amount_class": "text-success",
        },
        {
            "date": "Jan 29",
            "account": "Checking",
            "description": "Grocery Market",
            "amount": "-$84.12",
            "amount_class": "text-error",
        },
    ]

    context = {
        "active_nav": "dashboard",
        "due_accounts": due_accounts,
        "budget_legend": budget_legend,
        "budget_conic": budget_conic,
        "transactions": transactions,
    }
    return render(request, "ui/pages/dashboard.html", context)

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





