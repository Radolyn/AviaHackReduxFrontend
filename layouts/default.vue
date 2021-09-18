<template>

  <div>
    <nav class='navbar'>
      <button class='nav-burger' @click='burgerShow = !burgerShow'>
        <img height=15 width=30 src='../static/aviahack_burger.svg'>
      </button>

      <div class='burgerMenu' v-show=burgerShow>
        <nuxt-link to='/cellphone' style='border-bottom : 1px solid #B59797; border-radius: 5px 5px 0 0;'
                   class='burgerMenuItem'>
          <div class='row-start-1'>
            <span>Авторизация</span>
          </div>
        </nuxt-link>

        <nuxt-link to='/services' class='burgerMenuItem'>
          <div class='row-start-2'>
            <span>Услуги</span>
          </div>
        </nuxt-link>

        <nuxt-link to='/profile' style='border-top : 1px solid #B59797; border-radius: 0 0 5px 5px;' class='burgerMenuItem'>
          <div class='row-start-3'>
            <span>Личный кабинет</span>
          </div>
        </nuxt-link>
      </div>
    </nav>

    <div class='content' @click='burgerShow = false'>
      <nuxt/>
    </div>


    <br><br><br>
    <footer class='avia-footer' @click='burgerShow = false'>
      <div class='md:col-start-5 col-start-1 footerItem'>
        <a>
          <img src='../static/telegram.png' style='position : relative; top : 45px; left : 5px'>
        </a>
      </div>

      <div class='md:col-start-6 col-start-2 footerItem'>
        <a>
          <img src='../static/radolyn_vector1.png' style='position : relative; top : 20px; left : 5px'>
        </a>
      </div>

      <div class='md:col-start-7 col-start-3 footerItem'>
        <a>
          <img src='../static/github.png' style='position : relative; top : 45px; left : 5px'>
        </a>
      </div>
    </footer>
  </div>

</template>

<script>

export default {
  data() {
    return {
      burgerShow: false
    }

  },
}

</script>

<style src = './default.css'>
</style>

<style>
body, html {
  background-color: #EE5180;
}
</style>
