#!/usr/bin/node

exports.nbOccurences = fucntion(list, target)
{
    if (list === undefined || list.length === 0){
        return (0);
    }

    let occ = 0;
    for (let x = 0; x < list.length; x ++)
    {
        if (list[x] === target)
        {
            occ++;
        }
    }
    return (occ);
}