USERNAME = "ashaj079"  # define your MRU username here


def get_beverage_type(a_enabled: bool, b_enabled: bool) -> str:
    """
    Returns the beverage type defined by the switches.
    """
    if a_enabled == True and b_enabled == True:
        return 'Coffee, Latte,'
    elif a_enabled or b_enabled == True:
        return 'Tea, Earl Grey,'
    else:
        return 'Beer, IPA,'


def get_temperature_desc(slider_value: int) -> str:
    """
    Returns the temperature description defined by the slider value.
    Assume the value is always an integer between 0 and 100 (inclusive).
    """
    if slider_value == 0:
        return '''Frozen
                    _.-.  
                  ,'/ //\ 
                 /// // /)
                /// // //|
               /// // /// 
              /// // ///  
             (`: // ///   
              `;`: ///    
              / /:`:/     
             / /  `'      
            / /           
           (_/            
               '''
    elif 1 <= slider_value <= 16:
        return '''Cold   
    .   *   ..  . *  * 
*  * @()Ooc()*   o  .  
    (Q@*0CG*O()  ___   
    |\_________/|/ _ \ 
    |  |  |  |  | / | |
    |  |  |  |  | | | |
    |  |  |  |  | | | |
    |  |  |  |  | | | |
    |  |  |  |  | | | |
    |  |  |  |  | \_| |
    |  |  |  |  |\___/ 
    |\_|__|__|_/|      
    \_________/     
               '''
    elif 17 <= slider_value <= 40:
        return '''Warm
              ____     
             |    |    
             |    |    
             |____|    
             |    |    
             (    )    
             )    (    
           .'      `.  
          /          \ 
         |------------|
         |            |
         |   /----\   |
         |  |      |  |
         |  |      |  |
         |  |      |  |
         |   \----/   |
         |            |
         |------------|
         |____________|
                '''
    elif 41 <= slider_value <= 99:
        return '''Hot
         (  )   (   )  )      
          ) (   )  (  (       
          ( )  (    ) )       
          _____________       
         <_____________> ___  
          |             |/ _ \ 
          |               | | |
          |               |_| |
       ___|             |\___/ 
      /    \___________/    \  
      \_____________________/ 
               '''
    else:
        return '''Boiling
                        ( )    (  )
                 (  )              
               _.----""()""()---._ 
 .------.___  (     ()     ()     )
(        ___|-|`""----..(_)__..-""|
 \------/     |                   |
              |                   |
              |                   |
              |                   |
              `""----..____..---"" 
               '''


def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """
    if switch_name == 'a_enabled':
        a_enabled = input("Is switch A enabled? (y/n):")
        if a_enabled == 'y':
            return True
        else:
            return False

    if switch_name == 'b_enabled':
        b_enabled = input("Is switch B enabled? (y/n):")
        if b_enabled == 'y':
            return True
        else:
            return False


def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """

    switch_value_for_a = get_switch_value('a_enabled')
    switch_value_for_b = get_switch_value('b_enabled')
    slider_value = int(input("What is the value of the numeric slider? (0-100):"))
    print('result:', get_beverage_type(switch_value_for_a, switch_value_for_b), get_temperature_desc(slider_value))


main()

# faced a git function issue in terminal, credit to the fix goes to https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a
# for formatting the testing_log.md file in a fancy way, credit goes to https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax