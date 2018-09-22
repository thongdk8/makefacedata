#include "datamanager.h"
using namespace std;

int main(int argc, char *argv[])
{
    size_t dim = 128;
    size_t num_element = 5;
    int* id = new int[num_element];

    for(int i =0; i<num_element; i++)
        id[i] = 0;

    float* query = new float[128];
    for (int i =0; i< 128; i++){
        query[i] = i;
    }
    float* mass = new float[num_element*dim];
    for (int i = 0; i< num_element*dim; i++)
    {
        mass[i] = i;
    }

    std::string* names = new string[1];
    names[0] = "Testing";
    DataManager dm1;
    dm1.data = mass;
    dm1.id = id;
    dm1.vecdim = dim;
    dm1.names = names;
    dm1.nb_instance = num_element;
    dm1.nb_class = 1;
    dm1.knn = 30;
    dm1.threshold = 0.6;
    dm1.majority_threshold = 0.6;
    dm1.data_fn = "data.txt";
    dm1.name_data_fn = "name_data.txt";
    dm1.writeWholeData();
    dm1.updataParam(dm1.para_fn);


    std::cout << "Start registration" << std::endl;

    cout << argv[1] << endl;
    anet_type net;
    deserialize (argv[1]) >> net;

    DataManager dm("para.txt");
    dm.loadData ("data.txt", "name_data.txt");
    dm.initSearchEngine ();

    std::vector<std::string> namess;
    std::vector<int> ids;
    int nb_faces = -1;


    fstream meta_data;
    meta_data.open (argv[2]);
    meta_data >> nb_faces;

    cout << "read data, nb_faces " << nb_faces << endl;

    for (int i =0; i<nb_faces; i++)
    {
        int auto_id = -1;
        std::string name;
        cout << "read name" << endl;
        getline (meta_data, name);
        getline(meta_data, name);
        cout << "name" << name << endl;
        int id;
        meta_data >> id;
        int nb_im;
        meta_data >> nb_im;
        for (int j=0; j< nb_im; j++){
            std::string path;
            meta_data >> path;
            std::cout << "path" <<  path << std::endl;
            if (j==0)
                auto_id = dm.registerPerson (net, path, name, true);
            else
                dm.registerPerson(net, path, name, true, auto_id);
            cout << "registered id = " << auto_id << endl;
        }
    }

    cout << "finish registation!!!!!!!!!!!!!!!!!" << endl;

    return 0;

}
