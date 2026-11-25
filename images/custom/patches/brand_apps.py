
from pathlib import Path


BENCH = Path("/home/frappe/frappe-bench/apps")


def replace_once(file_path, old, new):
    path = BENCH / file_path
    content = path.read_text()

    count = content.count(old)

    if count != 1:
        raise RuntimeError(
            f"Expected exactly one match in {path}, found {count}"
        )

    path.write_text(content.replace(old, new, 1))
    print(f"Updated: {path}")


# Rename Frappe HR to ODA HR
replace_once(
    "hrms/hrms/hooks.py",
    'app_title = "Frappe HR"',
    'app_title = "ODA HR"',
)

replace_once(
    "hrms/hrms/hooks.py",
    '"title": "Frappe HR"',
    '"title": "ODA HR"',
)


# Rename Learning to ODA Learning
replace_once(
    "lms/lms/hooks.py",
    'app_title = "Learning"',
    'app_title = "ODA Learning"',
)

replace_once(
    "lms/lms/hooks.py",
    '"title": "Learning"',
    '"title": "ODA Learning"',
)


# Add Workspace and Company shortcuts to the New Apps screen

# Add Workspace and Company shortcuts to the New Apps screen
# Add Workspace and Company shortcuts to the New Apps screen
# Add custom workspace shortcuts to the New Apps screen
replace_once(
    "frappe/frappe/desk/page/desktop/desktop.js",
    "\t\t$('[data-toggle=\"tooltip\"]').tooltip({ placement: \"bottom\" });",
    """\t\t// ODA: Add frequently used ERPNext sections to the Apps screen.
\t\tconst workspace_shortcuts = [
\t\t\t{ label: "Accounting", route: "/app/accounting" },
\t\t\t{ label: "Assets", route: "/app/assets" },
\t\t\t{ label: "Projects", route: "/app/projects" },
\t\t\t{ label: "ERPNext Settings", route: "/app/erpnext-settings" },
\t\t\t{ label: "Organization", route: "/app/organization" },
\t\t];

\t\tworkspace_shortcuts.forEach((item) => {
\t\t\tthis.add_icon($grid, { label: item.label }, item.route);
\t\t});

\t\t$('[data-toggle="tooltip"]').tooltip({ placement: "bottom" });"""
)

print("ODA application branding and Apps screen shortcuts applied successfully.")
