from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera

# Create your views here.
def index(request):
    return render(request, 'index.html')
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def video_stream(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')

"""
Here content_type=’multipart/x-mixed-replace; boundary=frame’ is used to push the dynamically
 updated content to the web browser. This tells the browser to keep the connection open and replace
  the content according to the boundary.
  """

