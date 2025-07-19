# 🚀 AI SOCIAL BOT 🚀
# /dashboard.py

"""
CLI dashboard for the AI Social Bot.
"""

import argparse
import csv
import sqlite3

def list_leads(args):
    """
    Lists all leads in the database.
    """
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leads")
    rows = c.fetchall()
    conn.close()

    for row in rows:
        print(row)

def filter_by_tag(args):
    """
    Filters leads by tag.
    """
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leads WHERE tag=?", (args.tag,))
    rows = c.fetchall()
    conn.close()

    for row in rows:
        print(row)

def export_to_csv(args):
    """
    Exports all leads to a CSV file.
    """
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leads")
    rows = c.fetchall()
    conn.close()

    with open('leads.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'name', 'tag', 'last_contacted'])
        writer.writerows(rows)

    print("Leads exported to leads.csv")

def main():
    """
    Main function for the CLI dashboard.
    """
    parser = argparse.ArgumentParser(description="CLI dashboard for the AI Social Bot.")
    subparsers = parser.add_subparsers()

    # List leads command
    list_parser = subparsers.add_parser('list-leads', help='List all leads.')
    list_parser.set_defaults(func=list_leads)

    # Filter by tag command
    filter_parser = subparsers.add_parser('filter-tag', help='Filter leads by tag.')
    filter_parser.add_argument('tag', help='The tag to filter by.')
    filter_parser.set_defaults(func=filter_by_tag)

    # Export to CSV command
    export_parser = subparsers.add_parser('export', help='Export all leads to a CSV file.')
    export_parser.set_defaults(func=export_to_csv)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
