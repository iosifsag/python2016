import urllib2
import json

def print_data(data):
    print "\n\n\n\n"
    print "Title: " + data["Title"]
   
    print "IMDB Rating: " + data["imdbRating"]
   
    print "\n"

    print "Plot:"
    print data["Plot"]

    cont = raw_input("\n..")
    


def search(opt):
    try:
        omdbapi_url = "http://www.omdbapi.com/?"

        if opt == '1':
            title = raw_input("Movie Title: ")
            title = title.strip(' ')
            title = title.replace(' ', '+')

            omdbapi_url += "t=" + title
        else:
            movie_id = raw_input("Movie ID: ")
            movie_id = movie_id.strip(' ')

            omdbapi_url += "i=" + movie_id

        plot = raw_input("Plot (short,full): ")
        response = "json"

        url = omdbapi_url + "&y=&plot=" + str(plot) + "&r=" + str(response)

        req = urllib2.Request(url)
        result = urllib2.urlopen(req)
        data = result.read()
        json_data = json.loads(data)

        print_data(json_data)
    except KeyError:
        if opt == '1':
            print "Invalid movie title"
        else:
            print "Invalid movie ID"
        cont = raw_input("..")

search_opt = '1'
while search_opt != '0':
    print "Enter:"
    print "1 - Search by title"
    print "2 - Search by IMDb ID"
    print "0 - Exit"
    search_opt = raw_input("..")

    if search_opt != '0':
        search(search_opt)
