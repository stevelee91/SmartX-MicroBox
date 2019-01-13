type Idx: record {
        orig_h: addr;
};

type Val: record {
        orig_p: port &type_column="proto";
        resp_h: addr;
        resp_p: port &type_column="proto";
	ts: time;
	proto: string;
        service: string;
};
global blacklist: table[addr] of Val = table();

event bro_init() {
    Input::add_table([$source="list.file", $name="list",
                      $idx=Idx, $val=Val, $destination=blacklist]);
    Input::remove("list");
}
event Input::end_of_data(name: string, source: string) {
        # now all data is in the table
#        print blacklist;
#[i for i,l in enumerate(list) if '5' in l]
#any('555' in l for l in table) 
if (116.89.190.193 in blacklist)
 print "found black list entry";
if (116.89.190.201 in blacklist)
 print "found black list entry";

#elif (116.89.190.201 in blacklist)
#print "found black list entry";
print blacklist;
}
