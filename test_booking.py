from urllib import request, response
from endpoints.booking import Booking
from helpers.data_factory import build_booking
from helpers.requests import APIRequests
import allure # type: ignore

class TestClass:
    @allure.story("Booking API")
    @allure.title("Get Booking List")
    @allure.severity(allure.severity_level.NORMAL)
    def test_booking_list(self):
        bookingapi = Booking()
        response = bookingapi.get_booking_ids()
        status_code = response["status_code"]
        assert status_code == 200
        assert isinstance(response["data"], list)
        assert all(isinstance(item["bookingid"], int) for item in response["data"])

    @allure.story("Booking API")
    @allure.title("Create, Read and Delete Booking")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_CRUD_booking(self):
        bookingapi = Booking()
        apirequest = APIRequests()
        request_body = build_booking()
        response = bookingapi.create_booking(request_body)
        schema_validation = apirequest._load_json_schema("create_booking_schema.json")
        status_code = response["status_code"]
        print(response)
        bookingId = response["data"]["bookingid"]
        assert apirequest.assert_valid_schema(response["data"], schema_validation) == None
        assert status_code == 200
        assert response["data"]["booking"]["firstname"] == request_body["firstname"]

        get_response = bookingapi.get_booking(bookingId)
        assert get_response["status_code"] == 200
        assert get_response["data"] == request_body

        delete_response_status_code = bookingapi.delete_booking(bookingId)
        assert delete_response_status_code == 201

        assert bookingapi.get_booking(bookingId)["status_code"] == 404
