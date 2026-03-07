# python.ps1
while ($true) {
    # Ensure the pip module to be installed
    py -m ensurepip
    
    # Ensure that all packages are installed and updated
    py -m pip install --upgrade pip ruff customtkinter tk pytubefix
    
    # Run Ruff Formatting and Linting on the current directory
    py -m ruff format --check .
    
    # Wait for 1 hour
    Write-Host "Ruff completed at $(Get-Date). Waiting 20 minutes..."
    Start-Sleep -Seconds 1200
}
