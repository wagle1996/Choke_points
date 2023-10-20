import xarray as xr

# Path to your CMIP6 NetCDF file with monthly precipitation data (kg/m²/s)
data_file = 'path_to_your_cmip6_data.nc'

# Read the NetCDF file using xarray
data = xr.open_dataset(data_file)

# Extract the precipitation data (kg/m²/s) - Replace with the actual variable name
precipitation = data['precipitation']

# Define the number of seconds in a month (typically 30 days)
seconds_per_month = 2592000

# Convert kg/m²/s to kg/m²/month
precipitation_kg_per_m2_per_month = precipitation * seconds_per_month

# Resample to get yearly data (water year from October to September)
precipitation_water_year = precipitation_kg_per_m2_per_month.resample(time='AS-OCT').sum()

# Convert from kg/m²/year to m/year
# The density of water is approximately 1000 kg/m³, and 1 mm of water is equivalent to 1 kg/m²
conversion_factor = 1.0 / 1000.0  # kg/m²/year to m/year
precipitation_m_per_year = precipitation_water_year * conversion_factor

# Calculate the 30-year average
average_precipitation_m_per_year = precipitation_m_per_year.mean(dim='time')

# Save the resulting data to a new NetCDF file if desired
output_file = 'average_precipitation_m_per_year.nc'
average_precipitation_m_per_year.to_netcdf(output_file)

# Print the summary
print("30-year average precipitation data with units m/year has been calculated and saved to", output_file)
