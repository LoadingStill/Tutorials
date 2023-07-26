To test the HTTPS connection, you can use a web browser to navigate to 1https://localhost1. You may see a security warning from the browser, since the SSL certificate was self-signed and not issued by a trusted certificate authority. You can safely ignore this warning and proceed to the website.

If everything is set up correctly, you should see your Flask application in the web browser, with the URL starting with 1https://1. You can confirm that the connection is secure by clicking on the padlock icon in the address bar, which should show that the connection is encrypted with SSL.

Here's an example of what the browser might display:

![fbTssnZ](https://github.com/LoadingStill/Programming/assets/15201984/986aa0cd-a2bc-44a8-a753-a32bc9cee1b4)
HTTPS Connection

With these modifications, your Flask application should now be accessible over HTTPS with a self-signed SSL certificate.
