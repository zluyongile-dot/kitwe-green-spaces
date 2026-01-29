@echo off
echo 🚀 Final Deployment Steps
echo.

echo 📝 Adding all changes...
git add .

echo 💾 Committing changes...
git commit -m "Final deployment: Updated backend URLs for Railway"

echo 🌐 Pushing to GitHub...
git push origin main

echo.
echo ✅ Deployment complete!
echo 🌍 Your website: https://zluyongile-dot.github.io/kitwe-green-spaces/
echo 🔧 Backend status: Check Railway dashboard
echo.
pause