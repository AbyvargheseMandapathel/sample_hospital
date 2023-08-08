from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Appointment, Doctor, DoctorToken
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name')
        
        department = Department.objects.get(id=department_id)
        doctors = department.doctor_set.all()
        
        # Find the doctor with the fewest number of appointments and calculate token number
        selected_doctor = None
        min_appointments = float('inf')
        for doctor in doctors:
            appointments_count = Appointment.objects.filter(doctor=doctor).count()
            if appointments_count < min_appointments:
                selected_doctor = doctor
                min_appointments = appointments_count
        
        # Retrieve or create a DoctorToken object for the selected doctor
        doctor_token, created = DoctorToken.objects.get_or_create(doctor=selected_doctor)
        
        # Increment the doctor's token number
        doctor_token.token_number += 1
        doctor_token.save()
        
        appointment = Appointment.objects.create(
            name=name,
            mobile_number=mobile_number,
            department=department,
            doctor=selected_doctor,
            token_number=doctor_token.token_number
        )
        
        context = {
            'token_number': appointment.token_number,
            'doctor_name': selected_doctor.name  # Pass the doctor's name to the template
        }
        return render(request, 'visitors/appointment_success.html', context)


def index(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'visitors/index.html', context)
