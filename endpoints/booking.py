from helpers.requests import APIRequests

class Booking(APIRequests):
    def get_booking_ids(self):
        path = "/booking"
        response = self.get(path)
        return response

    def get_booking(self, bookingId):
        path = "/booking"
        full_path = path + "/" + str(bookingId)
        response = self.get(full_path)
        return response

    def create_booking(self, req):
        path = "/booking"
        response = self.post(path, req)
        return response

    def delete_booking(self, bookingId):
        path = "/booking"
        full_path = path + "/" + str(bookingId)
        response = self.delete(full_path)
        return response
