from setuptools import setup, find_packages


setup(name='hejtado-hardware',
      version="0.1.1",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      [console_scripts]
      hejtado-hardware = hejtado.hardware.hardware:main
      """)