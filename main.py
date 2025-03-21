from my_functions import build_experiment
from my_functions import build_person
from my_functions import estimate_max_hr
from datetime import datetime
if __name__ == "__main__":
    build_experiment (
        experiment_name='Maximale_HF',
        date='datetime',
        supervisor='Julius Mayr',
        subject='Maximale Leistung'
    )
    
    build_person (
        first_name='Simon',
        last_name='Schwarzer',
        sex='male',
        age=23
    )

    estimate_max_hr (
        age_years=23,
        sex='male'
    )
    print(int(max_hr_bpm))