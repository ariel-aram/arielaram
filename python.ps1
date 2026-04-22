# python.ps1
while ($true) {
    # Ensure the pip module to be installed
    python -m ensurepip
    
    # Ensure that all packages are installed and updated
    python -m pip install --upgrade pip ruff ty customtkinter tk pytubefix requests faker pandas openpyxl selenium webdriver-manager
    
    # Run Ruff Formatting and Linting on the current directory
    python -m ruff format --check
    python -m ty check --fix
    
    # Wait for 1 hour
    Write-Host "Ruff and ty check completed at $(Get-Date). Waiting 20 minutes..."
    Start-Sleep -Seconds 1200
}
