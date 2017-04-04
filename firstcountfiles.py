# will ignore lines in .ps1 files
# clear screen
cls

#sets the script path from the directory in which the script is running from :)
$PSScriptRoot = 'C:\Users\billy\Google Drive\Projects'

# STEP ONE get into the directory
cd 'C:\Users\billy\Google Drive\Projects'

# Get-ChildItem -Path 'C:\Users\billy\Google Drive\Projects' -Filter *.CR2 -Recurse -ErrorAction SilentlyContinue -Force
# Write-Host (Get-ChildItem -dir)
Write-Host (Get-ChildItem -dir -Recurse | ?{ $_.PSIsContainer } | Select-Object FullName)



echo "this is the folder you're working in"
Write-Host $PSScriptRoot
echo ""
echo ""
Write-Host ( Get-ChildItem $PSScriptRoot -Recurse -force *.CR2 | Measure-Object ).Count;

echo "the list of Reno Senior Pics"
# Write-Host ( Get-ChildItem 'C:\Users\billy\Google Drive\Jobs\2016-10-29 Kaitlyn Reny Senior Portraits\2016-10-29' | Measure-Object ).Count;
Get-ChildItem 'C:\Users\billy\Google Drive\Jobs\2016-10-29 Kaitlyn Reny Senior Portraits\2016-10-29' | Measure-Object

echo "Amount of .CR2 files in " $PSScriptRoot
Get-ChildItem -Recurse -force | Measure-Object

# return to the file directory for the script
cd 'C:\Users\billy\Dropbox\Github\filecountanddate\'


# write that directory to file
# count all files *.CR2
# apend that count to the file
# get up a directory
