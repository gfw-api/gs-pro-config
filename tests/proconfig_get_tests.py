import json
import os

import pytest

import proconfig


@pytest.fixture
def client():
    if not os.getenv('GATEWAY_URL'):
        raise Exception('GATEWAY_URL needs to be set')
    if not os.getenv('MICROSERVICE_TOKEN'):
        raise Exception('MICROSERVICE_TOKEN needs to be set')

    app = proconfig.app
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


valid_keys = [
    "cr_list_attributes", "cr_palm_risk_analysis", "fc_list_attributes", "historic_site_characteristics",
    "locations_alert_map",
    "loss_all_years", "mill_priority-history", "regions_idn_forest_moratorium_calc", "regions_idn_land_cover_calc",
    "regions_idn_legal_class_calc", "regions_prodes_annual", "regions_sa_annual", "regions_sa_biomes_calc",
    "regions_sea_annual",
    "regions_sea_land_cover_calc", "regions_soy_annual", "regions_soy_calculations", "sensitive_areas_historic_loss",
    "sensitive_areas_loss_annual", "threats", "threats_and_values", "trends_in_deforestation", "values"
]

reply_attributes = [
    'Change Answer Link',
    'Date last updated',
    "How it's Calculated",
    'Includes date range for Hansen data that needs to be updated',
    'Includes layers and/or calculations that will be updated before release 1',
    'Link to storage',
    'Notes',
    'Reason for update',
    'Response ID',
    'Technical Title', 'Timestamp',
    'Title',
    'What this Section Explains',
    'Why this Analysis?'
]


def test_get_invalid_key(client):
    response = client.get(
        '/api/v1/pro-config/fake')

    assert json.loads(response.data) == {'errors': [{
        'detail': 'Key fake not found. Valid keys are: cr_list_attributes, cr_palm_risk_analysis, fc_list_attributes, historic_site_characteristics, locations_alert_map, loss_all_years, mill_priority-history, regions_idn_forest_moratorium_calc, regions_idn_land_cover_calc, regions_idn_legal_class_calc, regions_prodes_annual, regions_sa_annual, regions_sa_biomes_calc, regions_sea_annual, regions_sea_land_cover_calc, regions_soy_annual, regions_soy_calculations, sensitive_areas_historic_loss, sensitive_areas_loss_annual, threats, threats_and_values, trends_in_deforestation, values',
        'status': 404}]}
    assert response.status_code == 404


def test_valid_keys(client):
    # WARNING: HERE BE DRAGONS!!! This test makes GET calls to an external google sheet, and validates that result. Changes in that spreadsheet may cause these tests to fail. You have been warned!
    for key in valid_keys:
        response = client.get(
            '/api/v1/pro-config/{}'.format(key))

        assert response.status_code == 200
        reply_json = json.loads(response.data)
        for reply_attribute in reply_attributes:
            assert reply_attribute in reply_json['data']
