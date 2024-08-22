async function fetchData (){

    const url = 'https://twinword-word-graph-dictionary.p.rapidapi.com/theme/?entry=mask';
    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': '1792edec30msh13684a097bd2034p106983jsn147060a62ac3',
            'x-rapidapi-host': 'twinword-word-graph-dictionary.p.rapidapi.com'
        }
    };
    
    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }


}