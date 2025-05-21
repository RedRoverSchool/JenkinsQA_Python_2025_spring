def test_open_load_statistics_page(manage_jenkins_page):
    load_stat_page = manage_jenkins_page.go_to_load_statistics_page()
    assert load_stat_page.get_title() == "Jenkins Load Statistics [Jenkins]", "Load statistics page title is incorrect"
