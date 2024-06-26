# Uncomment the required imports before adding the code

from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })
    return JsonResponse({"CarModels": cars})


# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data = {'userName': ''}
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False

    try:
        user = User.objects.get(username=username)
        username_exist = True
    except User.DoesNotExist:
        username_exist = False
    except Exception as e:
        username_exist = False
        print(f'An unexpected error occurred: {e}')

    try:
        user = User.objects.get(email=email)
        email_exist = True
    except User.DoesNotExist:
        email_exist = False
    except Exception as e:
        email_exist = False
        print(f'An unexpected error occurred: {e}')

    if not username_exist and not email_exist:
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)
    elif not username_exist and email_exist:
        data = {"userName": username, "error": "Email already registered"}
        return JsonResponse(data)
    else:
        data = {"userName": username, 'error': 'Username already taken'}
        return JsonResponse(data)


# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request, state="All"):
    if (state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = '/fetchReviews/dealer/' + str(dealer_id)
        reviews = get_request(endpoint)
        if reviews is not None:
            for review in reviews:
                sentiment = analyze_review_sentiments(review['review'])
                print(sentiment)
                review['sentiment'] = sentiment['sentiment']
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({
            "status": 400,
            "error": "Must specify a dealer id"
        })


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    if (dealer_id):
        endpoint = '/fetchDealer/' + str(dealer_id)
        dealerships = get_request(endpoint)
        return JsonResponse({"status": 200, "dealers": dealerships})
    else:
        return JsonResponse({
            "status": 400,
            "error": "Must specify a dealer id"
        })


# Create a `add_review` view to submit a review
def add_review(request):
    if not request.user.is_anonymous:
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            return JsonResponse({
                "status": 401,
                "message": f"Error in posting review: {e}"
            })
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})
