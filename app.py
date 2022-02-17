from subprocess import Popen
from types import MethodType
from typing import Container
from tempfile import NamedTemporaryFile
from flask import Flask, render_template, Response, \
  request, redirect, url_for
import pymysql.cursors, os, csv, io, pandas as pd, shutil
from OptimalRoadTripHtmlSaveAndDisplay import *

application = Flask(__name__)

# conn = cursor = None
# #fungsi koneksi database
# def openDb():
#    global conn, cursor
#    conn = pymysql.connect(host="localhost",user="root",passwd="",db="db_penjualan")
#    cursor = conn.cursor()	
# #fungsi untuk menutup koneksi
# def closeDb():
#    global conn, cursor
#    cursor.close()
#    conn.close()

#fungsi view index() untuk menampilkan data dari database
@application.route('/')
def index():   
   # openDb()
   # container = []
   # sql = "SELECT * FROM barang"
   # cursor.execute(sql)
   # results = cursor.fetchall()
   # for data in results:
   #    container.append(data)
   # closeDb()
   contacts = []
   with open("CityNgawi.csv") as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=",")
         for row in csv_reader:
            contacts.append(row)
         if (len(contacts) > 0):
            labels = contacts.pop(0)
        
   return render_template('tables.html', container=contacts,)	

@application.route('/map', methods=['GET','POST'])
def map():
   selesai = False  
   if request.method == 'POST':
      jgen = request.form['jgen']
      jpol = request.form['jpol']
      if request.form.get('go') == 'go':
            thisRunGenerations=int(jgen)
            thisRunPopulation_size=int(jpol)
            # pass
            # exec(open('OptimalRoadTripHtmlSaveAndDisplay.py').read())
            # os.system('python OptimalRoadTripHtmlSaveAndDisplay.py')
            GOOGLE_MAPS_API_KEY = "AIzaSyCK6wBEKMl4FJYDQPLS0zKL_GPoRpEPEJs"
            waypoints_file = "CityDistance.csv"

            #This is the general filename - as shorter routes are discovered the Population fitness score will be inserted into the filename
            #so that interim results are saved for comparision.  The actual filenames using the default below will be:
            #Output_<Population Fitness Score>.html 
            output_file = 'templates/Output.html'

            #parameters for the Genetic algoritim
            


            all_waypoints = ["HHV7+23G, Nambung, Waduk Pd., Bringin, Kabupaten Ngawi, Jawa Timur 63285, Indonesia",
                "Jl. Padepokan, Dari, Tawun, Kasreman, Kabupaten Ngawi, Jawa Timur 63281, Indonesia",
                "Pilang, Wonokerto, Pilang, Kawu, Kec. Kedunggalar, Kabupaten Ngawi, Jawa Timur 63254, Indonesia",
                "JF65+34G, Ngawi, Ngawi Sub-District, Ngawi Regency, East Java 63218, Indonesia",
                "Jl. Raya Solo-Ngawi Banjarejo, Kec. Kedunggalar, Kabupaten Ngawi, Jawa Timur 63254, Indonesia",
                "HJM6+FPV, Sumber Bening IV, Sumber Bening, Bringin, Kabupaten Ngawi, Jawa Timur 63285, Indonesia",
                "Jl. Rimau, Banjaran, Girikerto, Sine, Ngawi Regency, East Java 63264, Indonesia",
                "H6V3+472, Kauman, Widodaren, Ngawi Regency, East Java 63256, Indonesia",
                "C6HG+HGM, Hutan, Hutan Jogorogo, Jogorogo, Kabupaten Ngawi, Jawa Timur 63262, Indonesia",
                "F635+QQ2, Besek, Hargomulyo, Ngrambe, Kabupaten Ngawi, Jawa Timur 63263, Indonesia",
                "G4QW+2XP, Pohbebek, Tulakan, Sine, Kabupaten Ngawi, Jawa Timur 63264, Indonesia",
                "Jl. Water Park Tirtomolo, Sambi, Tempuran, Kec. Paron, Kabupaten Ngawi, Jawa Timur 63253, Indonesia",
                "Jl. Ngrambe - Jogorogo, Sola, Setono, Ngrambe, Kabupaten Ngawi, Jawa Timur 63263, Indonesia",
                "Depan SMP 1 Ngrambe Jl Musi No 12, RT. 04 RW. 05, Ngrambe, Ngawi, Sidorejo, Ngrambe, Kabupaten Ngawi, Jawa Timur 63263, Indonesia",
                "Jalan Tanpa Nama, Ngendut, Hargomulyo, Ngrambe, Kabupaten Ngawi, Jawa Timur 63263, Indonesia",
                "Sumberejo Sine, Area Kebun, Sumberejo, Sine, Kabupaten Ngawi, Jawa Timur 63264, Indonesia",
                "Dusun Brendil Provinsi, Hutan, Babadan, Kec. Paron, Kabupaten Ngawi, Jawa Timur 63253, Indonesia",
                "C6JX+PQ2, Gagar, Ngrayudan, Jogorogo, Kabupaten Ngawi, Jawa Timur 63262, Indonesia",
                "C5W9+77F, Pandansari, Sine, Kabupaten Ngawi, Jawa Timur 63264, Indonesia",
                "Jalan Tanpa Nama, Punen, Hargomulyo, Ngrambe, Kabupaten Ngawi, Jawa Timur 63263, Indonesia",
                "H8Q9+5GW, Ngarengan, Jenggrik, Kec. Kedunggalar, Kabupaten Ngawi, Jawa Timur 63254, Indonesia",
                "G7QM+VWV, Wonorejo, Kec. Kedunggalar, Kabupaten Ngawi, Jawa Timur 63254, Indonesia",
                "Jl. Poros, Putat, Tempuran, Kec. Paron, Kabupaten Ngawi, Jawa Timur 63253, Indonesia",
                "Jl. Ketanggung No.20, Krajan, Kuniran, Sine, Kabupaten Ngawi, Jawa Timur 63264, Indonesia",
                "C5P8+8CP Pariwisata wonosari, Gondangrejo, Wonosari, Sine, Kabupaten Ngawi, Jawa Timur 63264, Indonesia"]

            def CreateOptimalRouteHtmlFile(optimal_route, distance, display=True):
                  optimal_route = list(optimal_route)
                  optimal_route += [optimal_route[0]]

                  Page_1 = """
                  <!DOCTYPE html>
                  <html lang="en">
                     <head>
                     <meta charset="utf-8">
                     <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
                     <meta name="description" content="Randy Olson uses machine learning to find the optimal road trip across the U.S.">
                     <meta name="author" content="Randal S. Olson">
                     
                     <title>The optimal road trip across the U.S. according to machine learning</title>
                     <style>
                        html, body, #map-canvas {
                           height: 100%;
                           margin: 0px;
                           padding: 0px
                        }
                        #panel {
                           position: absolute;
                           top: 5px;
                           left: 50%;
                           margin-left: -180px;
                           z-index: 5;
                           background-color: #fff;
                           padding: 10px;
                           border: 1px solid #999;
                        }
                     </style>
                     <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCK6wBEKMl4FJYDQPLS0zKL_GPoRpEPEJs"></script>
                     <script>
                           var routes_list = []
                           var markerOptions = {icon: "http://maps.gstatic.com/mapfiles/markers2/marker.png"};
                           var directionsDisplayOptions = {preserveViewport: true,
                                                         markerOptions: markerOptions};
                           var directionsService = new google.maps.DirectionsService();
                           var map;

                           function initialize() {
                           var center = new google.maps.LatLng(-7.456496666933215, 111.35766776799072);
                           var mapOptions = {
                              zoom: 11,
                              center: center
                           };
                           map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
                           for (i=0; i<routes_list.length; i++) {
                              routes_list[i].setMap(map); 
                           }
                           }

                           function calcRoute(start, end, routes) {
                           
                           var directionsDisplay = new google.maps.DirectionsRenderer(directionsDisplayOptions);

                           var waypts = [];
                           for (var i = 0; i < routes.length; i++) {
                              waypts.push({
                                 location:routes[i],
                                 stopover:true});
                              }
                           
                           var request = {
                                 origin: start,
                                 destination: end,
                                 waypoints: waypts,
                                 optimizeWaypoints: true,
                                 travelMode: google.maps.TravelMode.DRIVING
                           };

                           directionsService.route(request, function(response, status) {
                              if (status == google.maps.DirectionsStatus.OK) {
                                 directionsDisplay.setDirections(response);      
                              }
                           });

                           routes_list.push(directionsDisplay);
                           }

                           function createRoutes(route) {
                              // Google's free map API is limited to 10 waypoints so need to break into batches
                              route.push(route[0]);
                              var subset = 0;
                              while (subset < route.length) {
                                 var waypointSubset = route.slice(subset, subset + 10);

                                 var startPoint = waypointSubset[0];
                                 var midPoints = waypointSubset.slice(1, waypointSubset.length - 1);
                                 var endPoint = waypointSubset[waypointSubset.length - 1];

                                 calcRoute(startPoint, endPoint, midPoints);

                                 subset += 9;
                              }
                           }
                  """
                  Page_2 = """
                           
                           createRoutes(optimal_route);

                           google.maps.event.addDomListener(window, 'load', initialize);

                     </script>
                     </head>
                     <body>
                     <div id="map-canvas"></div>
                     </body>
                  </html>
                  """

                  localoutput_file = output_file.replace('.html', '_' + str(distance) + '.html')
                  with open(localoutput_file, 'w') as fs:
                     fs.write(Page_1)
                     fs.write("\t\t\toptimal_route = {0}".format(str(optimal_route)))
                     fs.write(Page_2)

                  # if display:
                  #    webbrowser.open_new_tab(localoutput_file)


            def compute_fitness(solution):
                  """
                     This function returns the total distance traveled on the current road trip.
                     
                     The genetic algorithm will favor road trips that have shorter
                     total distances traveled.
                  """
                  
                  solution_fitness = 0.0
                  
                  for index in range(len(solution)):
                     waypoint1 = solution[index - 1]
                     waypoint2 = solution[index]
                     solution_fitness += waypoint_distances[frozenset([waypoint1, waypoint2])]
                     
                  return solution_fitness

            def generate_random_agent():
                  """
                     Creates a random road trip from the waypoints.
                  """
                  
                  new_random_agent = list(all_waypoints)
                  random.shuffle(new_random_agent)
                  return tuple(new_random_agent)

            def mutate_agent(agent_genome, max_mutations=3):
                  """
                     Applies 1 - `max_mutations` point mutations to the given road trip.
                     
                     A point mutation swaps the order of two waypoints in the road trip.
                  """
                  
                  agent_genome = list(agent_genome)
                  num_mutations = random.randint(1, max_mutations)
                  
                  for mutation in range(num_mutations):
                     swap_index1 = random.randint(0, len(agent_genome) - 1)
                     swap_index2 = swap_index1

                     while swap_index1 == swap_index2:
                           swap_index2 = random.randint(0, len(agent_genome) - 1)

                     agent_genome[swap_index1], agent_genome[swap_index2] = agent_genome[swap_index2], agent_genome[swap_index1]
                           
                  return tuple(agent_genome)

            def shuffle_mutation(agent_genome):
                  """
                     Applies a single shuffle mutation to the given road trip.
                     
                     A shuffle mutation takes a random sub-section of the road trip
                     and moves it to another location in the road trip.
                  """
                  
                  agent_genome = list(agent_genome)
                  
                  start_index = random.randint(0, len(agent_genome) - 1)
                  length = random.randint(2, 20)
                  
                  genome_subset = agent_genome[start_index:start_index + length]
                  agent_genome = agent_genome[:start_index] + agent_genome[start_index + length:]
                  
                  insert_index = random.randint(0, len(agent_genome) + len(genome_subset) - 1)
                  agent_genome = agent_genome[:insert_index] + genome_subset + agent_genome[insert_index:]
                  
                  return tuple(agent_genome)

            def generate_random_population(pop_size):
                  """
                     Generates a list with `pop_size` number of random road trips.
                  """
                  
                  random_population = []
                  for agent in range(pop_size):
                     random_population.append(generate_random_agent())
                  return random_population
            
            def run_genetic_algorithm(generations=int(jgen), population_size=int(jpol)):
                  """
                     The core of the Genetic Algorithm.
                     
                     `generations` and `population_size` must be a multiple of 10.
                  """
                  
                  current_best_distance = -1
                  population_subset_size = int(population_size / 10.)
                  generations_10pct = int(generations / 10.)
                  
                  # Create a random population of `population_size` number of solutions.
                  population = generate_random_population(population_size)

                  # For `generations` number of repetitions...
                  for generation in range(generations):
                     
                     # Compute the fitness of the entire current population
                     population_fitness = {}

                     for agent_genome in population:
                           if agent_genome in population_fitness:
                              continue

                           population_fitness[agent_genome] = compute_fitness(agent_genome)

                     # Take the top 10% shortest road trips and produce offspring each from them
                     new_population = []
                     for rank, agent_genome in enumerate(sorted(population_fitness,
                                                                  key=population_fitness.get)[:population_subset_size]):
                           if (generation % generations_10pct == 0 or generation == generations - 1) and rank == 0:
                              current_best_genome = agent_genome
                              print("Generation %d best: %d | Unique genomes: %d" % (generation,
                                                                                    population_fitness[agent_genome],
                                                                                    len(population_fitness)))
                              print(agent_genome)                
                              print("")

                              # If this is the first route found, or it is shorter than the best route we know,
                              # create a html output and display it
                              if population_fitness[agent_genome] < current_best_distance or current_best_distance < 0:
                                 current_best_distance = population_fitness[agent_genome]
                                 CreateOptimalRouteHtmlFile(agent_genome, current_best_distance, False)
                                 

                           # Create 1 exact copy of each of the top road trips
                           new_population.append(agent_genome)

                           # Create 2 offspring with 1-3 point mutations
                           for offspring in range(2):
                              new_population.append(mutate_agent(agent_genome, 3))
                              
                           # Create 7 offspring with a single shuffle mutation
                           for offspring in range(7):
                              new_population.append(shuffle_mutation(agent_genome))

                     # Replace the old population with the new population of offspring 
                     for i in range(len(population))[::-1]:
                           del population[i]

                     population = new_population
                  return current_best_genome
            # If this file exists, read the data stored in it - if not then collect data by asking google
            print("Begin finding shortest route")
            file_path = waypoints_file
            if os.path.exists(file_path):
               print("Waypoints exist")
               #file exists used saved results
               waypoint_distances = {}
               waypoint_durations = {}
               all_waypoints = set()

               waypoint_data = pd.read_csv(file_path, sep="\t")

               for i, row in waypoint_data.iterrows():
                     waypoint_distances[frozenset([row.waypoint1, row.waypoint2])] = row.distance_m
                     waypoint_durations[frozenset([row.waypoint1, row.waypoint2])] = row.duration_s
                     all_waypoints.update([row.waypoint1, row.waypoint2])

            else:
               # File does not exist - compute results       
               print("Collecting Waypoints")
               waypoint_distances = {}
               waypoint_durations = {}


               gmaps = googlemaps.Client(GOOGLE_MAPS_API_KEY)
               for (waypoint1, waypoint2) in combinations(all_waypoints, 2):
                     try:
                        route = gmaps.distance_matrix(origins=[waypoint1],
                                                      destinations=[waypoint2],
                                                      mode="driving", # Change to "walking" for walking directions,
                                                                     # "bicycling" for biking directions, etc.
                                                      language="English",
                                                      units="metric")

                        # "distance" is in meters
                        distance = route["rows"][0]["elements"][0]["distance"]["value"]

                        # "duration" is in seconds
                        duration = route["rows"][0]["elements"][0]["duration"]["value"]

                        waypoint_distances[frozenset([waypoint1, waypoint2])] = distance
                        waypoint_durations[frozenset([waypoint1, waypoint2])] = duration
               
                     except Exception as e:
                        print("Error with finding the route between %s and %s." % (waypoint1, waypoint2))
               
               print("Saving Waypoints")
               with open(waypoints_file, "w") as out_file:
                     out_file.write("\t".join(["waypoint1",
                                             "waypoint2",
                                             "distance_m",
                                             "duration_s"]))
               
                     for (waypoint1, waypoint2) in waypoint_distances.keys():
                        out_file.write("\n" +
                                       "\t".join([waypoint1,
                                                   waypoint2,
                                                   str(waypoint_distances[frozenset([waypoint1, waypoint2])]),
                                                   str(waypoint_durations[frozenset([waypoint1, waypoint2])])]))

            print("Search for optimal route")
            optimal_route = run_genetic_algorithm(generations=thisRunGenerations, population_size=thisRunPopulation_size)

            # This is probably redundant now that the files are created in run_genetic_algorithm,
            # but leaving it active to ensure  the final result is not lost
            CreateOptimalRouteHtmlFile(optimal_route, 1, True)
            selesai = True
   if selesai == True:
      return redirect(url_for('maphasil'))
   else:

            # print("Encrypted")
   #    elif  request.form.get('Decrypt') == 'Decrypt':
   #          # pass # do something else
   #          print("Decrypted")
   #    else:
   #          # pass # unknown
   #       return render_template("index.html")
   # elif request.method == 'GET':
   #    # return render_template("index.html")
   #    print("No Post Back Call")
   # return render_template("index.html") 
      return render_template('map.php')

# #fungsi view tambah() untuk membuat form tambah
@application.route('/tambah', methods=['GET','POST'])
def tambah():
#    if request.method == 'POST':
#       nama = request.form['nama']
#       harga = request.form['harga']
#       stok = request.form['stok']
#       openDb()
#       sql = "INSERT INTO barang (nama_barang, harga,stok) VALUES (%s, %s, %s)"
#       val = (nama, harga, stok)
#       cursor.execute(sql, val)
#       conn.commit()
#       closeDb()
#       return redirect(url_for('index'))
#    else:
#       return render_template('tambah.html')
   with open("CityNgawi.csv", mode='a+',newline='') as csv_file:
      fieldnames = ['City','Lat','Lon']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

      if request.method == 'POST':
         nama = request.form['nama']
         lat = request.form['lat']
         lon = request.form['lon']

         writer.writerow({'City':nama,'Lat':lat,'Lon':lon})
         return redirect(url_for('index'))
      else:
         return render_template('tambah.html')

# #fungsi view edit() untuk form edit
@application.route('/edit/<TeamCode>', methods=['GET','POST'])
def edit(TeamCode):
#    openDb()
#    cursor.execute('SELECT * FROM barang WHERE id_barang=%s', (id_barang))
#    data = cursor.fetchone()
#    if request.method == 'POST':
#       id_barang = request.form['id_barang']
#       nama = request.form['nama']
#       harga = request.form['harga']
#       stok = request.form['stok']
#       sql = "UPDATE barang SET nama_barang=%s, harga=%s, stok=%s WHERE id_barang=%s"
#       val = (nama, harga, stok, id_barang)
#       cursor.execute(sql, val)
#       conn.commit()
#       closeDb()
#       return redirect(url_for('index'))
#    else:
#       closeDb()
#       return render_template('edit.html', data=data)
   contacts = []

   with open("StadiumCoordinates.csv", mode="r") as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
         contacts.append(row)
   
   
   jos = []
   jos1 = []
   jos2 = []
   jos3 = []
   jos4 = []
   indeks = 0 
   for row in contacts:
      if row['TeamCode'] == TeamCode:
         jos = contacts[indeks]['TeamCode']
         jos1 = contacts[indeks]['TeamName']
         jos2 = contacts[indeks]['Stadium']
         jos3 = contacts[indeks]['Latitude']
         jos4 = contacts[indeks]['Longitude']
      indeks = indeks + 1

   # if len(ganti) > 0:
   #    jos = ganti['TeamCode']
   #    jos1 = ganti['TeamName']
   #    jos2 = ganti['Stadium']
   #    jos3 = ganti['Latitude']
   #    jos4 = ganti['Longitude']
   


   if request.method == 'POST':
      id = request.form['id']
      nama = request.form['nama']
      harga = request.form['harga']
      stok = request.form['stok']
      stok1 = request.form['stok1']
      
      # search and replace the contents
      # replace(str(jos), id) 
      # text = text.replace(str(jos1), nama) 
      # text = text.replace(str(jos2), harga) 
      # text = text.replace(str(jos3), stok) 
      # text = text.replace(str(jos4), stok1) 

      # filename = 'StadiumCoordinates.csv'
      # tempfile = NamedTemporaryFile(mode='w', delete=False)
      # fields = ['TeamCode','TeamName','Stadium','Latitude','Longitude']

      # with open(filename, 'r') as csvfile, tempfile:
      #    reader = csv.DictReader(csvfile, fieldnames=fields)
      #    writer = csv.DictWriter(tempfile, fieldnames=fields)
      #    for row in reader:
      #       if row['TeamCode'] == TeamCode:
      #          row['TeamCode'], row['TeamName'], row['Stadium'], row['Latitude'], row['Longitude'] = id, nama, harga, stok, stok1
      #       row = {'TeamCode': row['TeamCode'], 'TeamName': row['TeamName'], 'Stadium': row['Stadium'], 'Latitude': row['Latitude'], 'Longitude': row['Longitude']}
      #       writer.writerow(row)

      # shutil.move(tempfile.name, filename)
      return redirect(url_for('index'))
   else:

   # Menulis data baru ke file CSV (tulis ulang)
   # with open("StadiumCoordinates.csv", mode="w") as csv_file:
      # fieldnames = ['TeamCode','TeamName','Stadium','Latitude','Longitude']
      # writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      # for new_data in contacts:
      #    writer.writerow({'TeamCode': new_data['TeamCode'], 'TeamName': new_data['TeamName'], 'Stadium': new_data['Stadium'], 'Latitude': new_data['Latitude'], 'Longitude': new_data['Longitude']})
      return render_template('edit.html',jos=jos,jos1=jos1,jos2=jos2,jos3=jos3,jos4=jos4)
      



# #fungsi untuk menghapus data
@application.route('/hapus/<city>', methods=['GET','POST'])
def hapus(city):
#    openDb()
#    cursor.execute('DELETE FROM barang WHERE id_barang=%s', (id_barang,))
#    conn.commit()
#    closeDb()
#    return redirect(url_for('index'))
   contacts = []
   data = pd.read_csv('CityNgawi.csv')
   with open("CityNgawi.csv", mode="r") as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
         contacts.append(row)
   
      # indeks = 0
      # for data in contacts:
      #    if (data['TeamCode'] == TeamCode):
      #          contacts.remove(contacts[indeks])
      #    indeks = indeks + 1

      # data.drop(contacts['WAS'], inplace=True, axis=0)
      # Menulis data baru ke file CSV (tulis ulang)
      remove_specific_row_from_csv("CityNgawi.csv","City",city)
      return redirect(url_for('index'))

def remove_specific_row_from_csv(file, column_name, *args):
    '''
    :param file: file to remove the rows from
    :param column_name: The column that determines which row will be 
           deleted (e.g. if Column == Name and row-*args
           contains "Gavri", All rows that contain this word will be deleted)
    :param args: Strings from the rows according to the conditions with 
                 the column
    '''
    row_to_remove = []
    for row_name in args:
        row_to_remove.append(row_name)
    try:
        df = pd.read_csv(file)
        for row in row_to_remove:
            df = df[eval("df.{}".format(column_name)) != row]
        df.to_csv(file, index=False)
    except Exception  as e:
        raise Exception("Error message....")

@application.route('/mapku')
def mapku():
   return render_template('Output_1.html')

@application.route('/maphasil', methods=['GET','POST'])
def maphasil(): 

   return render_template('maphasil.php')


#----------------------------------------------------------------------------

if __name__ == '__main__':
   application.listen(process.env.PORT || 3000, function(){
      console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
   });
   application.run(debug=True)

