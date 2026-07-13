"""
modules.py

Central registry of all Oja test modules.
"""

from src.applications.oja.login import Login
from src.applications.oja.dashboard import Dashboard
from src.applications.oja.prescriptions import Prescriptions
from src.applications.oja.providers import Providers
from src.applications.oja.trackers import Trackers
from src.applications.oja.assessments import Assessments
from src.applications.oja.educationhub import EducationHub


MODULES = {

    "Login": Login,

    "Dashboard": Dashboard,

    "Prescriptions": Prescriptions,

    "Providers": Providers,

    "Trackers": Trackers,

    "Assessments": Assessments,

    "Education Hub": EducationHub

}