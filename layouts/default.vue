<template>

  <div>
    <nav class='navbar'>
      <button class='nav-burger' @click='burgerShow = !burgerShow'>
        <img height=15 width=30 src='../static/aviahack_burger.svg'>
      </button>

      <div class='burgerMenu' v-show=burgerShow>
        <nuxt-link to='/cellphone' style='border-bottom : 1px solid #B59797;'
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

        <nuxt-link to='/profile' style='border-top : 1px solid #B59797' class='burgerMenuItem'>
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
      <div class='md:col-start-5 col-start-1'>
        <a>
          <img src='../static/telegram.png' style='position : relative; top : 45px; left : 5px'>
        </a>
      </div>

      <div class='md:col-start-6 col-start-2'>
        <a>
          <img src='../static/radolyn_vector1.png' style='position : relative; top : 20px; left : 5px'>
        </a>
      </div>

      <div class='md:col-start-7 col-start-3'>
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

<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat&family=Montserrat:wght@300&family=Raleway:wght@300&family=Roboto:wght@300;500&display=swap');

body, html {
  background-color: #EE5180;
}

span {
  vertical-align: middle;
  font-weight: 800;
  font-family: 'Raleway', sans-serif;
}

.navbar {
  width : 100%;
  height: 75px;
  background: #403939;
  box-shadow: 0 8px 5px #574D4D;
}

.nav-burger {
  position: relative;
  float: right;
  margin-right: 30px;
  top: 28px;
}

.burgerMenu {
  z-index: 10;
  position: relative;
  float: right;
  top: 60px;
  left: 45px;
  background-color: #EBD2DA;
  color: #403939;
  padding: 4px;
  width: 185px;
  height: 130px;
  text-align: center;
  border-radius: 10px;
  box-shadow: 8px 8px 5px #574D4D;
  @apply grid grid-rows-3 grid-cols-1;
}

.burgerMenuItem {
  padding: 3px;
  border-radius: 5px 5px;
}

.burgerMenuItem:hover {
  background : #EE5180;
}

.content {
  min-height : 100vh;
  margin : 0;
  padding : 0;
}

.avia-footer {
  position : relative;
  margin-bottom : -140px;
  width: 100%;
  height: 140px;
  background: #403939;
  @apply grid md:grid-cols-11 sm:grid-cols-3 justify-items-center;
}

</style>
