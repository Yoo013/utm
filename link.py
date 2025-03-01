from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_shopee():
    referer = request.headers.get('Referer')
    
    if referer and 'facebook.com' in referer:
        utm_source = 'facebook'
    elif referer and 'instagram.com' in referer:
        utm_source = 'instagram'
    else:
        utm_source = 'other'
    
    # Redirect ke link Shopee dengan parameter UTM
    return redirect(f'https://shopee.co.id/product/1360283095/27861671532/?utm_source={utm_source}')

if __name__ == '__main__':
    app.run(debug=True)
