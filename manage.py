from jobplus.app import create_app

# use productionconfig

app = create_app('production')

if __name__ == '__main__':
	app.run()