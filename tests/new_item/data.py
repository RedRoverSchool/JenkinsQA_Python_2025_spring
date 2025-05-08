new_folder_name = 'Test_Folder'
new_freestyle_project_name = "Freestyle_Project"
expected_error = '» This field cannot be empty, please enter a valid name'
expected_item_types = [
    "Freestyle project",
    "Pipeline",
    "Multi-configuration project",
    "Folder",
    "Multibranch Pipeline",
    "Organization Folder"
]
expected_item_descriptions = [
    "Classic, general-purpose job type that checks out from up to one SCM, executes build steps serially, followed by post-build steps like archiving artifacts and sending email notifications.",
    "Orchestrates long-running activities that can span multiple build agents. Suitable for building pipelines (formerly known as workflows) and/or organizing complex activities that do not easily fit in free-style job type.",
    "Suitable for projects that need a large number of different configurations, such as testing on multiple environments, platform-specific builds, etc.",
    "Creates a container that stores nested items in it. Useful for grouping things together. Unlike view, which is just a filter, a folder creates a separate namespace, so you can have multiple things of the same name as long as they are in different folders.",
    "Creates a set of Pipeline projects according to detected branches in one SCM repository.",
    "Creates a set of multibranch project subfolders by scanning for repositories."
]
invalid_folder_name = 'Folder_does_not_exist'
copy_from_placeholder = 'No items'
