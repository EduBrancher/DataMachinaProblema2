# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:30:13 2021

@author: Windows
"""

from __future__ import annotations



class Volume:
    
    def __init__(self, largura, espessura, altura):
        
        self.largura = largura
        self.espessura = espessura
        self.altura = altura
        self.volume = self.largura * self.espessura * self.altura
        
        self.dimensions = [largura, espessura, altura]
        self.dimensions.sort(reverse=True)
        
        self.largest_dimension = self.dimensions[0]
        self.middle_dimension = self.dimensions[1]
        self.lesser_dimension = self.dimensions[2]
        
        pass
    

    
    def imprima(self):

        print("Largura: " + str(self.largura))
        print("Altura: " + str(self.altura))
        print("Espessura: " + str(self.espessura))
        print("Volume: " + str(self.volume))
        print("Dimensions: " + str(self.dimensions))
        print("lar_dim: " + str(self.largest_dimension))
        print("mid_dim: " + str(self.middle_dimension))
        print("less_dim: " + str(self.lesser_dimension) + "\n")
        
        pass
    
    def fits_in(self, other: Volume):
        
        if (self.largest_dimension <= other.largest_dimension and
            self.middle_dimension <= other.middle_dimension and
            self.lesser_dimension <= other.lesser_dimension):
            return(True)
        else:
            return(False)
        
        pass
    


class Item:
    
    def __init__(self, peso, largura, espessura, altura):
        
        self.volume = Volume(largura, espessura, altura)
        self.peso = peso
        
        pass
    
    def imprima(self):
        
        print("Peso: " + str(self.peso))
        self.volume.imprima()
        
        pass
    
    pass

class Vehicle:
    
    def __init__(self, dono, tipo, largura, altura, espessura, peso):
        
        self.item = Item(peso, largura, espessura, altura)
        self.dono = dono
        self.tipo = tipo
        
        pass
    
    def imprima(self):
        print("Dono: " + str(self.dono))
        print("Tipo: " + str(self.tipo))
        self.item.imprima()
        pass
    
    pass
    
    

def create_vehicles():
    
    vehicle_list = []
    file = open("veiculos.txt", "r")
    vehicles = file.read().splitlines()
    file.close()
    
    for vehicle in vehicles:
        
        attrlist = vehicle.split()
        vehicle_list.append(Vehicle(attrlist[0], attrlist[1], int(attrlist[2]),
                                    int(attrlist[3]), int(attrlist[4]), int(attrlist[5])))
        pass
    
    for vehicle in vehicle_list:
        vehicle.imprima()
        
        pass
    
    return(vehicle_list)
    pass

def list_items(arq):
    
    
    ret_list = []
    file = open(arq, "r")
    itemlist = file.read().splitlines()
    file.close()
    
    for item in itemlist:
        
        attrlist = item.split()
        
        for i in range(0, len(attrlist)):
            attrlist[i] = int(attrlist[i])
            pass
        
        newitem = Item(attrlist[0], attrlist[1], attrlist[2], attrlist[3])
        newitem.imprima()
        ret_list.append(newitem)
        
        pass
    
    ret_list.sort(reverse=True, key=vol_item)
    return(ret_list)
    
    pass

def vol_volume(vol: Volume):
    return(vol.volume)
    pass

def vol_item(item: Item):
    return(item.volume.volume) 
    pass

def vol_vehicle(ve : Vehicle):
    return(ve.item.volume.volume)
    pass

def separate_by_owner(lista):
    
    owner = lista[0].dono
    ownerlists = []
    retlist = []
    
    for item in lista:
        if (item.dono == owner):
            retlist.append(item)
        else:
            ownerlists.append(retlist)
            retlist = []
            owner = item.dono
            retlist.append(item)
        pass
    
    ownerlists.append(retlist)
    for lista in ownerlists:
        lista.sort(key=vol_vehicle)
    return(ownerlists)

    pass

def determine_secondary_volumes(fitteditem, container):
    
    secondary_volumes = []
    #print("fitted: " + str(fitteditem.volume.dimensions))
    #print("container: " + str(container.dimensions))
    
    if (container.lesser_dimension == container.altura):
        #print("1")
        secondary_volumes.append(Volume(container.largest_dimension - fitteditem.volume.largest_dimension,
                                                        fitteditem.volume.middle_dimension, 
                                                        fitteditem.volume.lesser_dimension))
                       
        secondary_volumes.append(Volume(fitteditem.volume.largest_dimension,
                                        container.middle_dimension - fitteditem.volume.middle_dimension,
                                        fitteditem.volume.lesser_dimension))
                        
        secondary_volumes.append(Volume(container.largest_dimension - fitteditem.volume.largest_dimension,
                                        container.middle_dimension - fitteditem.volume.middle_dimension,
                                        fitteditem.volume.lesser_dimension))
        pass
    elif (container.middle_dimension == container.altura):
        #print("2")
        secondary_volumes.append(Volume(container.largest_dimension - fitteditem.volume.largest_dimension,
                                        fitteditem.volume.lesser_dimension,
                                        fitteditem.volume.middle_dimension))
        secondary_volumes.append(Volume(fitteditem.volume.largest_dimension,
                                        container.lesser_dimension - fitteditem.volume.lesser_dimension,
                                        fitteditem.volume.middle_dimension))
        secondary_volumes.append(Volume(container.largest_dimension - fitteditem.volume.largest_dimension,
                                        container.lesser_dimension - fitteditem.volume.lesser_dimension,
                                        fitteditem.volume.middle_dimension))
        pass
    elif (container.largest_dimension == container.altura):
        #print("3")
        secondary_volumes.append(Volume(container.middle_dimension - fitteditem.volume.middle_dimension,
                                        fitteditem.volume.lesser_dimension,
                                        fitteditem.volume.largest_dimension))
        secondary_volumes.append(Volume(fitteditem.volume.middle_dimension,
                                        container.lesser_dimension - fitteditem.volume.lesser_dimension,
                                        fitteditem.volume.largest_dimension))
        secondary_volumes.append(Volume(container.middle_dimension - fitteditem.volume.middle_dimension,
                                        container.lesser_dimension - fitteditem.volume.lesser_dimension,
                                        fitteditem.volume.largest_dimension))
        
        pass
    #print("gerados pela funcao: ")
    #for item in secondary_volumes:
    #    print(str(item.dimensions))
    
    return(secondary_volumes)
    pass

#this is the one
    
def fit_items_to_vehicles(itemlist, ownerlists):
    
    result_list = [] #devolve uma lista com números. o primeiro número refere-se ao veículo 
                     #que deve ser usado pela primeira companhia, o segundo ao veículo que
                     #deve ser usado pela segunda, etc. por exemplo:
                     #[0, 2] : A companhia 0 deve usar seu veículo 0 e a 1 deve usar o veículo 2.
                     #Se não couber em nenhum veículo de uma, retorna -1 naquela posição.
    company_counter = 0;
    for company in ownerlists:
        result_list.append(-1)
    
    for company in ownerlists: #cada companhia tem um conjunto de veiculos:
        print("C. counter: " + str(company_counter))
        vehicle_counter = 0; #current vehicle
        
        for vehicle in company: #company é uma lista de objetos veículo
            print("V. counter: " + str(vehicle_counter))
            vol = vehicle.item.volume
            print("Cur. vol: ")
            vol.imprima()
            i = 0
            proc = 1
            items_weight = 0 #peso total dos itens é o primeiro cutoff
            fitted = [] #fitted[i] = 1 se o item i está no veiculo, 0 se nao        
            for item in itemlist:
                fitted.append(0)
                pass
            
            for item in itemlist:
                items_weight = items_weight + item.peso
                pass
            if (items_weight > vehicle.item.peso): #muito pesado para este veículo
                print("Weight fail\n")
                vehicle_counter = vehicle_counter + 1
                continue
                pass
                        
            while (i < len(itemlist) and proc == 1):
                
                if (fitted[i] == 1):
                    i = i + 1
                    continue 
                if (itemlist[i].volume.fits_in(vol)):
                    print(str(itemlist[i].volume.dimensions) + " initially fitted.\n")
                    fitted[i] = 1
                    secondary_volumes = []
                      
                    secondary_volumes = determine_secondary_volumes(itemlist[i], vol)
                        
                    secondary_volumes.sort(reverse=True, key=vol_volume)
                    print("Secondary volumes: ")
                    for volum in secondary_volumes:
                        print(str(volum.dimensions))
                    print("")
                    for volum in secondary_volumes:
                        j = 0
                        while j < len(itemlist):
                            if (fitted[j] == 0):
                                if (itemlist[j].volume.fits_in(volum)):
                                    print(str(itemlist[j].volume.dimensions) + " fitted in " + str(volum.dimensions))
                                    fitted[j] = 1
                                    break                                
                                pass
                                print(str(itemlist[j].volume.dimensions) + " failed to fit.")
                            j = j + 1
                            pass
                        pass
                    
                    if (vol.largest_dimension == vol.altura):
                        vol = Volume(vol.largura, vol.espessura, vol.altura - itemlist[i].volume.largest_dimension)
                    elif (vol.middle_dimension == vol.altura):
                        vol = Volume(vol.largura, vol.espessura, vol.altura - itemlist[i].volume.middle_dimension)
                    elif (vol.lesser_dimension == vol.altura):
                        vol = Volume(vol.largura, vol.espessura, vol.altura - itemlist[i].volume.lesser_dimension)
                    print("Remaining vol after last fitting series: " + str(vol.dimensions))
                    print("")
                    pass  
                else:
                    proc = 0
                i = i + 1
                pass
           
            finished = 1
            for i in range(0, len(fitted)):
                if (fitted[i] == 0):
                    finished = 0
                pass
            if (finished == 1):
                result_list[company_counter] = vehicle_counter
                break
            vehicle_counter = vehicle_counter + 1
            pass
        
        company_counter = company_counter + 1
        pass
        
    return(result_list)
    pass