from flask import Flask, request, jsonify
from libs.lib import *

app = Flask(__name__)
app.json.sort_keys = False
@app.route('/getbestpath', methods=['POST', 'GET'])
def getbestpath():

    if request.method == 'POST':
        data = request.json
        if data.get('lang') != None:
            if data.get('source') != None and data.get('dist') != None:
                if data.get('lang').upper() == 'ENGLISH':

                    if check_match_name(station=str(data.get('dist'))) != 1:
                        dist = check_match_name(station=str(data.get('dist')))
                    else:
                        return jsonify('error-source'), 200
                    if check_match_name(station=str(data.get('source'))) != 1:
                        source = check_match_name(
                            station=str(data.get('source')))
                    else:
                        return jsonify('error-dist'), 200
                    best_path_list_en = find_best_path_en(
                        source=source, dist=dist)

                    res = {'stations': best_path_list_en,
                           'time': len(best_path_list_en)*3}

                    return jsonify(res), 200

                elif data.get('lang').upper() == 'FARSI':

                    if check_match_name(station=str(data.get('dist'))) != 1:

                        dist = check_match_name(station=str(data.get('dist')))

                    else:
                        if check_match_name(station=str(data.get('source'))) == 1:

                            return jsonify('error-dist-source'), 200
                        else:
                            return jsonify('error-dist'), 200

                    if check_match_name(station=str(data.get('source'))) != 1:

                        source = check_match_name(
                            station=str(data.get('source')))

                    else:

                        if check_match_name(station=str(data.get('dist'))) == 1:

                            return jsonify('error-dist-source'), 200
                        else:
                            return jsonify('error-source'), 200

                    best_path_list_fa = find_best_path_fa(
                        source=source, dist=dist)
                    
                    res = {'stations': best_path_list_fa,
                           'time': len(best_path_list_fa)*3}
                    return jsonify(res), 200
            else:
                if data.get('source') == None:

                    return 'The source argument is required', 400

                if data.get('dist') == None:

                    return 'The dist argument is required', 400
        else:
            return 'The lang argument can be Farsi or English :)', 400

    if request.method == 'GET':

        return 'For more information : https://github.com/mohamadrzm/Metrogo-Core', 405
