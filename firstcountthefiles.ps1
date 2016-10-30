# will ignore lines in .bat files

cls

#sets the script path from the directory in which the script is running from :)
$scriptpath = $PSScriptRoot

echo ""
echo "This Script will run in this directory"
Write-Host $PSScriptRoot
echo ""
echo ""
# nothing else #smiles


# # Write-Host ( Get-ChildItem 'C:\Users\billy\Google Drive\Jobs\2016-10-29 Kaitlyn Reny Senior Portraits\2016-10-29' | Measure-Object ).Count;
