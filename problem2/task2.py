import json

allData = {
    "annotations": [
        {
            "result": []
        }
    ],
    "data": {
        "image": "\/data\/upload\/image1.jpg"
    }
}

def txtTOjsn (FolderPath):
    with open(FolderPath) as f:
        for line in f:
            obj = {}
            data = line.split()
            fields = ['x', 'y', 'width', 'height']
            i = 0
            while i < len(fields):
                obj[fields[i]] = float(data[i+1])
                i+=1
            #Adding rotation explicitly because it is not in the array
            obj["rotation"] = 0
            #Check the object type based on the first value
            if (data[0] == '0'):
                obj["rectanglelabels"] = ["object"]
            else:
                obj["rectanglelabels"] = ["unknown"]
            sample = {
                "image_rotation" : 0,
                "values" : obj
            }
            allData["annotations"][0]["result"].append(sample)

    # creating json file
    out_file = open("result.json", "w")
    json.dump(allData, out_file, indent=4)
    out_file.close()


txtTOjsn("Write the text file path")

        
