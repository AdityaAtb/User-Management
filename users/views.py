from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from mongoengine import DoesNotExist, ValidationError
from .models import User


@api_view(['GET'])
def get_user_by_id(request, id):
    try:
        user = User.objects.get(id=id)
        return Response(user.to_json(), status=status.HTTP_200_OK)
    except DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        return Response({'error': 'Invalid ID format'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_all_users(request):
    try:
        users = User.objects.all()
        user_list = [u.to_json() for u in users]
        return Response(user_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_new_user(request):
    try:
        new_user = User(**request.data)
        new_user.save()
        return Response({
            'message': 'User registered successfully!',
            'user': new_user.to_json()
        }, status=status.HTTP_201_CREATED)
    except ValidationError:
        return Response({'error': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
        for field, value in request.data.items():
            setattr(user, field, value)
        user.save()
        return Response({
            'message': 'User details updated successfully',
            'user': user.to_json()
        }, status=status.HTTP_200_OK)
    except DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        return Response({'error': 'Invalid data format'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
    except DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        return Response({'error': 'Invalid id format'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)