import json
import base64
import io
import pygame
from common.constants import StatusCode
from django.core.cache import cache
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from songs.models import Song
from users.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes

# Create your views here.


#@csrf_exempt
@ensure_csrf_cookie
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload_song(request):
    print(request.user.email)
    print(request.auth.key)
    user = Token.objects.get(key=request.auth.key).user

    body = json.loads(request.body)
    song_name = body.get('songName', '')
    song_base64 = body.get('base64', '')
    difficulty = body.get('difficulty', 'Any')
    bpm = body.get('bpm', 0)

    # print(song_base64)

    # play_song(song_base64)
    save_song(user, song_name, song_base64, difficulty, bpm)

    return JsonResponse({
        'message': 'Successfully uploaded: ' + song_name
    }, status=StatusCode.OK)


def play_song(song_base64):
    pygame.mixer.init()
    sound_file_data = base64.b64decode(song_base64)
    #assert sound_file_data.startswith(b'OggS')  # just to prove it is an Ogg Vorbis file
    sound_file = io.BytesIO(sound_file_data)
    # The following line will only work with VALID data. With above example data it will fail.
    sound = pygame.mixer.Sound(sound_file)
    ch = sound.play()
    while ch.get_busy():
        pygame.time.wait(100)

def save_song(user, song_name, song_base64, difficulty, bpm):
    print('======================starting to upload=============================')
    song = Song(user=user)
    song.song_original.save(song_name, ContentFile(song_base64.encode('utf-8')))
    song.difficulty = difficulty
    song.bpm = bpm
    song.save()

    # cache.set('song', song)
    print('*****successfully uploaded ' + song_name + ' to GCloud*****')
    print('======================completed   upload=============================')

def delete_song(user, song_name):
    #song = Song()
    pass