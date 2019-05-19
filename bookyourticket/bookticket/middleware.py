from bookticket.models import ClientRequest
class REQTrack:
	def __init__(self, view):
		self.view_fun = view

	def __call__(self, request):
		#to check the reuest
		url = request.META["PATH_INFO"]
		ipa= request.META["REMOTE_ADDR"]
		cr = ClientRequest(url=url, ip_adress=ipa)
		cr.save()
		resp  =self.view_fun(request)
		cr.resp_status = resp.status_code
		cr.save()
		# to check the response
		return resp