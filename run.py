from myapp import create_app

application = create_app()

if __name__ == '__main__':
    print("RUNNING APPLICATION NOW")
    application.run(host='0.0.0.0', port = 9000)