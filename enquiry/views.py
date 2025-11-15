from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializers import EnquirySerializer

import gspread
from google.oauth2.service_account import Credentials

# Google Sheet setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file("google-credentials.json", scopes=SCOPE)
CLIENT = gspread.authorize(CREDS)
SHEET = CLIENT.open("Event Enquiries").sheet1  # Create a sheet named 'Event Enquiries' in your Google Drive

@api_view(['POST'])
def create_enquiry(request):
    serializer = EnquirySerializer(data=request.data)
    if serializer.is_valid():
        enquiry = serializer.save()

        # Push to Google Sheets
        SHEET.append_row([
            enquiry.name,
            enquiry.contact_number,
            enquiry.email,
            enquiry.event_type,
            enquiry.num_persons,
            enquiry.preferred_location,
            enquiry.event_date.strftime("%Y-%m-%d"),
            enquiry.requirements,
        ])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render

def home(request):
    return render(request, 'enquiry/home.html')

def enquiry_page(request):
    return render(request, 'enquiry/enquiry.html')

def contact_page(request):
    return render(request, "enquiry/contact.html")

