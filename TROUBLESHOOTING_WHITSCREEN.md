# Troubleshooting White Screen

## Steps to Debug

1. **Open Browser Console** (F12)
   - Look for red error messages
   - Check Console tab
   - Check Network tab for failed requests

2. **Common Issues**
   - Import errors
   - Component rendering errors
   - API connection issues
   - Missing dependencies

3. **Quick Fix: Check Browser Console**

Please open the browser console (F12) and share any error messages you see.

The white screen usually means there's a JavaScript error preventing React from rendering.

## Likely Causes

1. **Import path issues** - The `@/` alias might not be resolving
2. **Component errors** - One of the new components has a syntax error
3. **API errors** - The metadata service isn't responding

## Next Steps

Please check the browser console and share the error message. That will tell us exactly what's wrong.
