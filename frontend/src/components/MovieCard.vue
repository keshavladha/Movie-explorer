<template>
  <div class="movie-card">
    <h3 class="text-xl font-bold text-gray-900 mb-2">{{ movie.title }}</h3>
    <p class="text-gray-600 mb-2">{{ movie.release_year }}</p>
    
    <div class="mb-3">
      <p class="text-sm text-gray-700" v-if="movie.director">
        <strong>Director:</strong> 
        <router-link 
          :to="`/director/${movie.director.id}`" 
          class="text-primary-600 hover:text-primary-800"
        >
          {{ movie.director.name }}
        </router-link>
      </p>
    </div>

    <div class="mb-4" v-if="movie.synopsis">
      <p class="text-gray-700 text-sm line-clamp-3">{{ movie.synopsis }}</p>
    </div>

    <div class="flex justify-between items-center">
      <span class="text-sm text-gray-500" v-if="movie.duration">
        {{ movie.duration }} min
      </span>
      <router-link 
        :to="`/movie/${movie.id}`" 
        class="btn-primary text-sm"
      >
        View Details
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { MovieSummary } from '@/types'

defineProps<{
  movie: MovieSummary
}>()
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style> 