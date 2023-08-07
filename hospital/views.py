from django.shortcuts import render
from django.db.models import Q
from visitors.models import Appointment , Doctor , Department , DoctorToken

def appointments_list(request):
    search_query = request.GET.get('q', '')
    doctor_group = request.GET.get('doctor_group', '')
    department_filter = request.GET.get('department_filter', '')  # Retrieve the selected department filter value

    # Retrieve all appointments
    appointments = Appointment.objects.all()
    doctors = Doctor.objects.all()  # Retrieve doctors from the visitor app
    departments = Department.objects.all()  # Retrieve departments from the visitor app

    # Filter appointments based on search query
    if search_query:
        appointments = appointments.filter(
            Q(name__icontains=search_query) | Q(mobile_number__icontains=search_query)
        )

    # Filter appointments based on selected doctor group
    if doctor_group:
        appointments = appointments.filter(doctor_id=doctor_group)

    # Filter appointments based on selected department filter
    if department_filter:
        appointments = appointments.filter(department_id=department_filter)

    context = {
        'appointments': appointments,
        'doctors': doctors,
        'departments': departments,
    }
    return render(request, 'hospital/appointments_list.html', context)
