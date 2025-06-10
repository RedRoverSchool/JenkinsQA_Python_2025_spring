from tests.freestyle_project import freestyle_data


def test_not_advanced_checkboxes(create_empty_job_with_api, main_page):
    job_name = create_empty_job_with_api["job_name"]
    freestyle_conf_page = (main_page
                           .go_to_freestyle_project_page(job_name)
                           .go_to_configure())
    where = f"on {freestyle_conf_page.__class__.__name__}"

    all_displayed_checkboxes = freestyle_conf_page.get_all_displayed_checkboxes()
    all_checkboxes_names = freestyle_conf_page.get_all_checkboxes_names()

    assert freestyle_conf_page.is_enable(), \
        f"Freestyle project is not enabled by default {where}."

    assert len(all_displayed_checkboxes) == 16, f"Unexpected number of checkboxes {where}."

    assert all_checkboxes_names == freestyle_data.Configuration.NOT_ADVANCED_CHECKBOXES_TEXTS, \
        f"Unexpected checkboxes names have been found {where}."

