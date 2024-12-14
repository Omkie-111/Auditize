import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import json
from .services.title_generator import generate_blog_title
from .services.audio_transcription import transcribe_audio


@csrf_exempt
def transcription_view(request):
    """
    View to handle audio transcription requests.
    """
    if request.method == "POST":
        if 'audio_file' not in request.FILES:
            return JsonResponse({"error": "No audio file uploaded."}, status=400)

        audio_file = request.FILES['audio_file']

        # Saving the file to a temporary location
        file_path = default_storage.save(audio_file.name, audio_file)
        file_path = default_storage.path(file_path)

        try:
            # Calling the transcription service asynchronously
            transcription_response = asyncio.run(transcribe_audio(file_path))
            
            return JsonResponse(transcription_response, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            default_storage.delete(file_path)

    return JsonResponse({"message": "Send a POST request with an audio file."}, status=400)

@csrf_exempt
def title_suggestions(request):
    """
    API endpoint to generate blog title suggestions.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            content = body.get("content", "")
            
            if not content:
                return JsonResponse({"error": "Blog content is required"}, status=400)
            
            # Generating the title
            title = generate_blog_title(content)
            return JsonResponse({"title": title})
        
        except ValueError as ve:
            return JsonResponse({"error": str(ve)}, status=400)
        except RuntimeError as re:
            return JsonResponse({"error": str(re)}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)