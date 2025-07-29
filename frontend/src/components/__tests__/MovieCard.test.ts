import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createRouter, createWebHistory } from 'vue-router'
import MovieCard from '../MovieCard.vue'
import type { MovieSummary } from '@/types'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: { template: 'Home' } },
    { path: '/movie/:id', component: { template: 'Movie' } },
    { path: '/director/:id', component: { template: 'Director' } }
  ]
})

const mockMovie: MovieSummary = {
  id: 1,
  title: 'Test Movie',
  release_year: 2023,
  synopsis: 'A test movie synopsis',
  duration: 120,
  director: {
    id: 1,
    name: 'Test Director',
    birth_year: 1980
  }
}

describe('MovieCard', () => {
  it('renders movie information correctly', () => {
    const wrapper = mount(MovieCard, {
      props: { movie: mockMovie },
      global: {
        plugins: [router]
      }
    })

    expect(wrapper.text()).toContain('Test Movie')
    expect(wrapper.text()).toContain('2023')
    expect(wrapper.text()).toContain('Test Director')
    expect(wrapper.text()).toContain('120 min')
  })

  it('handles missing synopsis gracefully', () => {
    const movieWithoutSynopsis = { ...mockMovie, synopsis: undefined }
    const wrapper = mount(MovieCard, {
      props: { movie: movieWithoutSynopsis },
      global: {
        plugins: [router]
      }
    })

    expect(wrapper.find('.text-gray-700').exists()).toBe(false)
  })

  it('handles missing director gracefully', () => {
    const movieWithoutDirector = { ...mockMovie, director: undefined }
    const wrapper = mount(MovieCard, {
      props: { movie: movieWithoutDirector },
      global: {
        plugins: [router]
      }
    })

    expect(wrapper.text()).not.toContain('Director:')
  })
}) 