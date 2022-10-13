try:
    import lightrun
    lightrun.enable(company_key='e3282e3e-89a9-4b91-b82a-7d8ca0f33cb7')
except ImportError as e:
    print("Error importing Lightrun: ", e)