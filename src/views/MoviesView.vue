<template>
    <h1>Movies</h1>
    <div class="cards" >
        <div class="card" v-for="movie in movies">
            <div class="left">
                <img :src=movie.poster>
            </div>
            <div class="right">
                <div class="title"><h3>{{ movie.title }}</h3></div>
                <div class="desc">{{ movie.description }}</div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import {ref, onMounted} from 'vue'

    let movies = ref([])

    onMounted(() => {
         fetchMovies()
    })

    const fetchMovies = () => {
        fetch("/api/v1/movies")
        .then(res => res.json())
        .then(data => {
            console.log(data)
            movies.value = data.movies
        })
        .catch(err => console.log(err))
    }
</script>

<style>

    body{
        padding: 70px;
    }

    .cards {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-flow:row wrap;
        width: 90%;
        margin: 0 auto;
    }

    /* .cards::after {
        content: "";
        flex: auto;
    } */

    .card {
        display: flex;
        flex-direction: row;
        width: 650px;
        height: 300px;
        margin: 10px auto;
        overflow: hidden;
        margin: 20px;
    }

    .card > .left > img {
        width: 220px;
        height: 300px;
    }

    .card > .right {
        padding: 30px;
    }

</style>