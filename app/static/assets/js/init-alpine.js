function data() {
  function getThemeFromLocalStorage() {
    // if user already changed the theme, use it
    if (window.localStorage.getItem('dark')) {
      return JSON.parse(window.localStorage.getItem('dark'))
    }

    // else return their preferences
    return (
      !!window.matchMedia &&
      window.matchMedia('(prefers-color-scheme: dark)').matches
    )
  }

  function setThemeToLocalStorage(value) {
    window.localStorage.setItem('dark', value)
  }

  return {
    dark: getThemeFromLocalStorage(),
    toggleTheme() {
      this.dark = !this.dark
      setThemeToLocalStorage(this.dark)
    },
    isSideMenuOpen: false,
    toggleSideMenu() {
      this.isSideMenuOpen = !this.isSideMenuOpen
    },
    closeSideMenu() {
      this.isSideMenuOpen = false
    },
    isNotificationsMenuOpen: false,
    toggleNotificationsMenu() {
      this.isNotificationsMenuOpen = !this.isNotificationsMenuOpen
    },
    closeNotificationsMenu() {
      this.isNotificationsMenuOpen = false
    },
    isProfileMenuOpen: false,
    toggleProfileMenu() {
      this.isProfileMenuOpen = !this.isProfileMenuOpen
    },
    closeProfileMenu() {
      this.isProfileMenuOpen = false
    },
    isPagesMenuOpen: false,
    togglePagesMenu() {
      this.isPagesMenuOpen = !this.isPagesMenuOpen
    },
    // lend modal
    isLendBookModalOpen: false,
    lendTrapCleanup: null,
    openLendBookModal() {
      this.isLendBookModalOpen = true
      this.lendTrapCleanup = focusTrap(document.querySelector('#LendModal'))
    },
    closeLendBookModal() {
      this.isLendBookModalOpen = false
      this.lendTrapCleanup()
    },
    // receive modal
    isReceiveBookModalOpen: false,
    receiveTrapCleanup: null,
    openReceiveBookModal() {
      this.isReceiveBookModalOpen = true
      this.receiveTrapCleanup = focusTrap(document.querySelector('#ReceiveModal'))
    },
    closeReceiveBookModal() {
      this.isReceiveBookModalOpen = false
      this.receiveTrapCleanup()
    },
    
  }
}