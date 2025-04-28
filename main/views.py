from django.shortcuts import render, redirect, get_object_or_404
from pytubefix import YouTube
from .models import YoutubeVideo
import os
from django.http import HttpResponse, StreamingHttpResponse
from .forms import VideoForm
# Create your views here.

def homepage(request):
    context = {
        'form' : VideoForm()
    }
    if request.method == 'POST':
        
        form = VideoForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            yt = YouTube(url)

            yt_vid = YoutubeVideo(title = yt.title, thumbnail_url =  yt.thumbnail_url, url = url)
            yt_vid.save()

            context = {
                'title' : yt.title,
                'thumbnail' : yt.thumbnail_url,
                'yt_vid' : yt_vid,
                'form' : VideoForm()
            }
            
        
        return render(request, 'homepage.html', context)
    
        
    return render(request, 'homepage.html', context)

def download_content(request, vid_id):
    if request.method == 'POST':
        yt_vid = get_object_or_404(YoutubeVideo, id = vid_id)
        try:
            yt = YouTube(yt_vid.url)
            stream = yt.streams.get_by_itag(18)

            def video_streaming_generator():
                for chunk in stream.iter_chunks(chunk_size=4096):
                    yield chunk
            
            response = StreamingHttpResponse(video_streaming_generator(), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{yt_vid.title}.mp4"'

            
            yt_vid.delete()
            return response
        except Exception as e: 
            return HttpResponse(f"An error occured {e}")
